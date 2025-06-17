# src/api/routers/chat.py
from fastapi import APIRouter, HTTPException, Request
import json
from sse_starlette.sse import EventSourceResponse
from api.schemas.chat import ChatRequest, ChatResponse
# from..services import llm_factory
from api.my_agent.agent import get_graph


router = APIRouter()

@router.post("/invoke", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Receives a chat request, gets an LLM from the factory,
    and returns the model's response.
    """
    try:
        graph = get_graph()
        config = {"configurable": {"thread_id": request.thread_id}}
        input_messages = [msg.model_dump() for msg in request.messages]  # TODO Prepare messages for the model

        # 3. Invoke the model
        response = await graph.ainvoke({"messages": input_messages}, config=config)
        final_message = response["messages"][-1]
        
        return ChatResponse(
            output=final_message,
            thread_id=request.thread_id
        )

    except Exception as e:
        # It's good practice to handle exceptions
        raise HTTPException(status_code=500, detail=str(e))
    

async def stream_generator(request_body: ChatRequest):
    """
    An async generator that streams the agent's response.
    """
    graph = get_graph()
    config = {"configurable": {"thread_id": request_body.thread_id}}
    input_messages = [msg.model_dump() for msg in request_body.messages]
    
    # Use astream to get an async iterator of the final response chunks.
    # The 'messages' mode streams only the message content.
    async for chunk in graph.astream({"messages": input_messages}, config=config, stream_mode="messages"):
        if not chunk:
            continue
        
        # The last message in the list is the one being generated.
        agent_response_chunk = chunk[-1]
        
        # Format the chunk as a JSON string for the SSE event.
        # The client will parse this to update the UI.
        yield {
            "event": "data",
            "data": json.dumps({
                "role": agent_response_chunk.role,
                "content": agent_response_chunk.content
            })
        }


@router.post("/stream-sse")
async def chat_stream_sse(request_body: ChatRequest):
    """
    Receives a chat request and streams the agent's response using Server-Sent Events (SSE).
    """
    return EventSourceResponse(stream_generator(request_body))