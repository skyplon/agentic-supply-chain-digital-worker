import streamlit as st
import time
import random

from agent import call_llm
from tools import (
    check_inventory,
    get_impacted_orders,
    find_alternative_supplier,
    update_order_status
)

st.set_page_config(page_title="AI Supply Chain Agent", layout="wide")

# HEADER
st.title("🤖 Autonomous Supply Chain Digital Worker")
st.caption("Powered by LLM reasoning + tool orchestration (simulated enterprise integrations)")

st.markdown(
    "This prototype simulates an **AI digital worker** that detects, analyzes, plans, and executes supply chain decisions."
)

# AGENT STATUS
st.info("🤖 Agent initialized. Monitoring supply chain events and ready to respond...")

# INPUT
user_input = st.text_input("📩 Enter disruption event:")

# RUN BUTTON
if st.button("🚀 Run Agent"):

    if not user_input:
        st.warning("Please enter a disruption event.")
    else:

        st.divider()

        # Helper function
        def run_step(title, func, allow_retry=False):
            container = st.container()
            with container:
                st.markdown(f"### 🤖 {title}")
                status = st.empty()

                status.info("🟡 Thinking...")
                time.sleep(1.2)

                # Simulate occasional failure (low probability)
                failed = allow_retry and random.random() < 0.2

                if failed:
                    status.error("🔴 Temporary failure detected. Retrying...")
                    time.sleep(1)
                    status.info("🟡 Retrying...")
                    time.sleep(1)

                result = func()

                status.success("🟢 Completed")
                st.write(result)

            return result

        # STEP 1 — PLANNER (LLM reasoning)
        with st.expander("🧠 Planner Agent — Reasoning Trace", expanded=True):
            reasoning = run_step(
                "Step 1: Understanding the Problem (Planner Agent)",
                lambda: call_llm(user_input)
            )

        # Identify product
        from agent import detect_product

        product = detect_product(user_input)

        # STEP 2 — IMPACT
        impacted = run_step(
            "Step 2: Impact Analysis (Executor Agent)",
            lambda: get_impacted_orders(product)
        )

        # STEP 3 — INVENTORY
        inventory_status = run_step(
            "Step 3: Inventory Check (Executor Agent)",
            lambda: check_inventory(product),
            allow_retry=True
        )

        # STEP 4 — SUPPLIER
        supplier = run_step(
            "Step 4: Mitigation Strategy (Executor Agent)",
            lambda: find_alternative_supplier(product)
        )

        # STEP 5 — ACTION
        update = run_step(
            "Step 5: Execution (Executor Agent)",
            lambda: update_order_status(1),
            allow_retry=True
        )

        st.divider()

        # FINAL DECISION
        st.markdown("## 🤖 Final Decision")

        st.success(
            f"""
            The agent autonomously resolved the disruption for **{product}**  
            → Selected mitigation: **{supplier}**  
            → Updated impacted orders and minimized disruption
            """
        )

        # CONFIDENCE SCORE
        confidence = random.randint(85, 98)

        st.markdown("### 🧠 Agent Confidence Score")
        st.progress(confidence / 100)
        st.write(f"Confidence Level: **{confidence}%**")

        # BUSINESS IMPACT
        st.markdown("## 📊 Business Impact")

        col1, col2, col3 = st.columns(3)

        col1.metric("Orders Saved", "3")
        col2.metric("Delay Reduced", "2 days")
        col3.metric("Manual Effort", "High ↓")

        st.divider()

        # SYSTEM NOTE
        st.caption(
            "Note: This prototype simulates agent orchestration, tool usage, and decision-making in a controlled environment."
        )