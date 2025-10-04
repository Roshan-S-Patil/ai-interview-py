from typing import Any, Dict
from configs.langchain_config import get_langchain_app, get_langchain_app_async
from langchain_core.messages import HumanMessage, AIMessage

# synchronous version
# services/chat_service.py
from configs.langchain_config import get_langchain_app, get_langchain_app_async
from langchain_core.messages import HumanMessage, AIMessage

# Synchronous handler
def handle_chat(thread_id: str, incoming_messages: list[dict]) -> list[dict]:
    # Lazy initialize LangChain app (cached, reused)
    app = get_langchain_app()

    msgs = []
    for m in incoming_messages:
        role = m.get("role")
        content = m.get("content")
        if role == "human":
            msgs.append(HumanMessage(content=content))
        elif role == "ai":
            msgs.append(AIMessage(content=content))

    output = app.invoke(
        {"messages": msgs},
        config={"configurable": {"thread_id": thread_id}}
    )

    # new_messages = output["messages"]
    # return [{"role": msg.__class__.__name__.lower(), "content": msg.content} for msg in new_messages]
    new_message = output["messages"][-1]
    return [{"role": new_message.__class__.__name__.lower(), "content": new_message.content}]


# Asynchronous handler
async def handle_chat_async(thread_id: str, incoming_messages: list[dict]) -> list[dict]:
    # Lazy initialize async LangChain app (cached, reused)
    app = await get_langchain_app_async()

    msgs = []
    for m in incoming_messages:
        role = m.get("role")
        content = m.get("content")
        if role == "human":
            msgs.append(HumanMessage(content=content))
        elif role == "ai":
            msgs.append(AIMessage(content=content))

    output = await app.ainvoke(
        {"messages": msgs},
        config={"configurable": {"thread_id": thread_id}}
    )

    last_msg = output["messages"][-1]
    return [{"role": last_msg.__class__.__name__.lower(), "content": last_msg.content}]
