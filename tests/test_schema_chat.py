from datetime import datetime

from langchain_core.messages import AIMessage

from app.schemas.chat import ChatRequest, ChatResponse


def test_chat_request_model():
    req = ChatRequest(message="Hello!", thread_id="thread-123")
    assert req.thread_id == "thread-123"
    assert isinstance(req.message[0], str)
    assert req.message == "Hello!"


def test_chat_response_model():
    ai_msg = AIMessage(content="Hi there!")
    now = datetime.now()
    resp = ChatResponse(output=ai_msg, thread_id="thread-123", timestamp=now)
    assert resp.thread_id == "thread-123"
    assert isinstance(resp.output, AIMessage)
    assert resp.output.content == "Hi there!"
    assert resp.timestamp == now
