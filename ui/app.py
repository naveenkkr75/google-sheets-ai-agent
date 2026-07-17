import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import streamlit as st
import matplotlib.pyplot as plt

from dashboard.stats import (
    get_inventory_dataframe,
    get_inventory_stats,
)

from prompts import SYSTEM_PROMPT
from agent.graph import agent
from langchain_core.messages import SystemMessage


st.set_page_config(
    page_title="Google Sheets AI Agent",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Google Sheets AI Agent")

# --------------------------
# Load Data
# --------------------------

df = get_inventory_dataframe()

stats = get_inventory_stats(df)

# --------------------------
# Dashboard Cards
# --------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Products", stats["products"])
c2.metric("Total Value", f"₹{stats['total_value']:,}")
c3.metric("Average Price", f"₹{stats['average_price']:,}")
c4.metric("Max Price", f"₹{stats['max_price']:,}")

st.divider()

# --------------------------
# Charts
# --------------------------

if not df.empty:

    st.subheader("Inventory Price Chart")

    fig, ax = plt.subplots(figsize=(8,4))

    ax.bar(
        df["Product Name"],
        df["Price"],
    )

    ax.set_xlabel("Product")

    ax.set_ylabel("Price")

    st.pyplot(fig)

st.divider()

# --------------------------
# Inventory Table
# --------------------------

st.subheader("Inventory")

st.dataframe(
    df,
    use_container_width=True,
)

st.divider()

# --------------------------
# AI Chat
# --------------------------

st.subheader("AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask me anything...")

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    response = agent.invoke(
        {
            "messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                {
                    "role": "user",
                    "content": query,
                },
            ]
        },
        config={
            "configurable": {
                "thread_id": "streamlit"
            }
        }
    )

    final = response["messages"][-1]

    answer = ""

    if isinstance(final.content, str):

        answer = final.content

    else:

        for item in final.content:

            if item.get("type") == "text":
                answer += item["text"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.rerun()