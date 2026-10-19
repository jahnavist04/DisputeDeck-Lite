import os
import json
import streamlit as st
from huggingface_hub import InferenceClient
st.set_page_config(
    page_title="DisputeDeck Lite",
    page_icon="🧾",
    layout="wide",
)
st.title("🧾 DisputeDeck Lite")
st.subheader("AI-powered dispute preparation for online sellers")
st.write(
    "Organize customer complaints, identify missing evidence, "
    "and prepare professional replies."
)
st.info(
    "Use fictional data for testing. Your case details are sent "
    "to the configured hosted AI provider when you analyze a case."
)


def get_secret(name, default=""):
    try:
        value = st.secrets.get(name, "")
        if value:
            return value
    except Exception:
        pass
    return os.getenv(name, default)


def analyze_dispute(case):
    token = get_secret("HF_TOKEN")
    model = get_secret(
        "HF_MODEL",
        "Qwen/Qwen2.5-7B-Instruct",
    )

    if not token:
        raise ValueError(
            "HF_TOKEN is missing. Configure it in Streamlit secrets."
        )

    client = InferenceClient(
        model=model,
        token=token,
        timeout=90,
    )

    system_prompt = """
You are DisputeDeck Lite, an assistant for small online sellers.

Analyze the seller's dispute information carefully.
Never invent facts, tracking details, policies, or evidence.
Separate supplied facts from uncertain points.
Do not assume either party is lying.
Suggest useful evidence to collect.
Write a polite, calm, professional customer reply.
Do not promise refunds or replacements unless the seller says
they have already been approved.
Do not provide legal guarantees.

Return ONLY valid JSON with these keys:
{
  "known_facts": ["fact"],
  "uncertain_points": ["point"],
  "missing_evidence": ["evidence item"],
  "suggested_reply": "professional reply",
  "risk_note": "important caution"
}
"""

    response = client.chat_completion(
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": json.dumps(case, ensure_ascii=False),
            },
        ],
        max_tokens=1200,
        temperature=0.2,
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("The AI returned an empty response.")

    content = content.strip()

    if content.startswith("```"):
        content = content.removeprefix("```json")
        content = content.removeprefix("```")
        content = content.removesuffix("```").strip()

    result = json.loads(content)

    required = {
        "known_facts",
        "uncertain_points",
        "missing_evidence",
        "suggested_reply",
        "risk_note",
    }

    if not required.issubset(result):
        raise ValueError("The AI returned an incomplete response.")

    return result


st.divider()
st.header("1. Enter dispute details")

with st.form("dispute_form"):
    col1, col2 = st.columns(2)

    with col1:
        order_id = st.text_input(
            "Order reference",
            placeholder="DEMO-1042",
        )
        amount = st.text_input(
            "Order amount",
            placeholder="₹850",
        )
        platform = st.selectbox(
            "Sales platform",
            ["Instagram", "WhatsApp", "Facebook", "Marketplace", "Other"],
        )

    with col2:
        issue = st.selectbox(
            "Type of complaint",
            [
                "Item not received",
                "Item damaged",
                "Wrong item received",
                "Refund requested",
                "Payment dispute",
                "Other",
            ],
        )
        status = st.selectbox(
            "Order status",
            [
                "Not shipped",
                "Shipped",
                "Marked delivered",
                "Status unknown",
                "Not applicable",
            ],
        )

    order_details = st.text_area(
        "What was ordered and agreed?",
        placeholder="Describe the order and any agreed terms.",
    )

    complaint = st.text_area(
        "Customer complaint",
        placeholder="What did the customer say happened?",
        height=130,
    )

    st.write("**Evidence already available**")

    evidence_options = [
        "Order confirmation",
        "Payment receipt",
        "Customer conversation",
        "Dispatch or tracking details",
        "Delivery confirmation",
        "Product photos",
        "Refund or return policy",
    ]

    evidence = []

    evidence_cols = st.columns(3)

    for i, item in enumerate(evidence_options):
        with evidence_cols[i % 3]:
            if st.checkbox(item, key=f"available_{i}"):
                evidence.append(item)

    additional = st.text_area(
        "Additional information (optional)",
        placeholder="Relevant dates or actions already taken.",
    )

    submitted = st.form_submit_button(
        "Analyze dispute",
        type="primary",
        use_container_width=True,
    )


if submitted:
    if not complaint.strip():
        st.error("Enter the customer complaint first.")
    elif not order_details.strip():
        st.error("Describe the order first.")
    else:
        case = {
            "order_reference": order_id.strip() or "Not provided",
            "amount": amount.strip() or "Not provided",
            "platform": platform,
            "complaint_type": issue,
            "order_status": status,
            "order_details": order_details.strip(),
            "customer_complaint": complaint.strip(),
            "evidence_available": evidence,
            "additional_information": additional.strip() or "None provided",
        }

        try:
            with st.spinner("Analyzing the dispute with AI..."):
                result = analyze_dispute(case)

            st.session_state["result"] = result
            st.session_state["case"] = case

        except Exception as error:
            st.error("Could not analyze the dispute.")
            st.code(str(error))
            st.caption(
                "Check your Hugging Face token, model availability, "
                "inference permissions, and provider limits."
            )


result = st.session_state.get("result")

if result:
    st.divider()
    st.header("2. Case analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Facts provided")
        for fact in result["known_facts"]:
            st.markdown(f"- {fact}")

    with col2:
        st.subheader("Uncertain points")
        for point in result["uncertain_points"]:
            st.markdown(f"- {point}")

    st.divider()
    st.header("3. Missing-evidence checklist")
    st.caption("Tick items only after you have actually collected them.")

    for i, item in enumerate(result["missing_evidence"]):
        st.checkbox(item, key=f"missing_{i}")

    st.divider()
    st.header("4. Professional reply generator")

    reply = st.text_area(
        "Edit your reply before sending",
        value=result["suggested_reply"],
        height=180,
        key="reply_editor",
    )

    st.caption("Select the reply above and press Ctrl+C to copy it.")

    st.subheader("Important caution")
    st.warning(result["risk_note"])

    st.download_button(
        "Download case summary",
        data=json.dumps(
            {
                "case": st.session_state["case"],
                "analysis": result,
                "edited_reply": reply,
            },
            ensure_ascii=False,
            indent=2,
        ),
        file_name="disputedeck-summary.json",
        mime="application/json",
    )

st.divider()
st.caption(
    "DisputeDeck Lite | Open-weight AI for clearer dispute preparation"
)
