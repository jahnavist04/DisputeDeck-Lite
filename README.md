# 🧾 DisputeDeck Lite

### Open-weight AI for smarter customer dispute preparation

**DisputeDeck Lite** is an AI-powered assistant designed for small online sellers who sell through Instagram, WhatsApp, and other online platforms. It helps sellers organize customer complaints, identify missing evidence, and draft professional responses when a sale doesn't go as expected.

🔗 **[Live Demo](https://disputedeck-lite.streamlit.app/)** · **[GitHub Repository](https://github.com/jahnavist04/DisputeDeck-Lite)**

---

## 💡 The Problem

Small online sellers often handle customer complaints without dedicated support teams or dispute-management tools. When a customer reports a missing item, damaged product, or refund issue, sellers may struggle to organize the available information and decide what to check before replying.

DisputeDeck Lite provides a simple way to structure the case, identify unanswered questions, and prepare a clear, professional response.

## ✨ Features

- **📝 Dispute Case Form:** Enter order details, complaint type, order status, and additional context.
- **🤖 AI-Powered Case Analysis:** Separate provided facts from uncertain points.
- **📋 Missing-Evidence Checklist:** Identify potentially useful evidence to collect before responding.
- **💬 Professional Reply Generator:** Generate an editable, respectful response to the customer.
- **📥 Case Summary Export:** Download the case information and analysis as a JSON file.
- **🌐 Web-Based Interface:** Access the application through a browser without installing a desktop application.

## 🛠️ Tech Stack

- **Python** — application logic
- **Streamlit** — interactive web interface
- **Hugging Face Inference Providers** — hosted model inference
- **Open-weight instruction model** — dispute analysis and reply generation

## 🚀 Try the Live Demo

Visit **[disputedeck-lite.streamlit.app](https://disputedeck-lite.streamlit.app/)**.

1. Enter the order details.
2. Describe the customer's complaint.
3. Select the evidence already available.
4. Click **Analyze dispute**.
5. Review the facts, uncertainties, and suggested evidence.
6. Edit the generated customer reply before using it.
7. Download the case summary if needed.

For your first test, use fictional order information and a sample complaint.

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/jahnavist04/DisputeDeck-Lite.git
cd DisputeDeck-Lite
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Hugging Face

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token
HF_MODEL=Qwen/Qwen2.5-7B-Instruct
```

Replace the example model ID if needed with a model supported by your Hugging Face Inference Providers account.

Create your token at [Hugging Face Access Tokens](https://huggingface.co/settings/tokens).

**Never commit your `.env` file or expose your access token publicly.**

### 5. Start the application

```bash
streamlit run app.py
```

Open the local URL printed in your terminal.

## 🌍 Why Open-Source AI?

Open-source and open-weight AI can make AI-powered tools more accessible to developers, students, and small businesses. Developers can inspect, adapt, and build upon available models instead of having to train a model from scratch.

DisputeDeck Lite demonstrates how an open-weight model can be integrated into a practical workflow that addresses a real challenge for small online sellers.

The project is intended as a starting point for experimentation, community contributions, and future improvements.

## 🔐 Privacy and Responsible Use

- Avoid entering passwords, payment-card details, or unnecessary personal information.
- Submitted case text is sent to the configured hosted inference provider for analysis.
- AI-generated analysis may be incomplete or incorrect. Verify important details against the actual evidence.
- Suggested evidence is a checklist of possible next steps, not proof of either party's claims.
- Review and edit every generated reply before sending it.
- DisputeDeck Lite does not provide legal advice or guarantee dispute outcomes.

## 🗺️ Future Improvements

- [ ] Add downloadable PDF case reports.
- [ ] Improve structured analysis and error handling.
- [ ] Add multilingual complaint analysis.
- [ ] Introduce reusable case history with privacy-conscious storage.
- [ ] Add automated tests for the case-analysis workflow.
- [ ] Improve accessibility and responsive UI design.

## 🤝 Contributing

Contributions, suggestions, bug reports, and feature ideas are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application.
5. Submit a pull request describing your changes.

Please do not commit credentials, private customer data, or confidential order information.

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---
**Built for small online sellers, with open-weight AI.** 🧾🤖
`#devchallenge` `#hf26challenge`
