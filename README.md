## 🤖 USJ AI Master's Program Chatbot

This project is a conversational AI assistant developed using [Rasa](https://rasa.com/) to support prospective students interested in the Artificial Intelligence Master's program at Université Saint-Joseph (USJ). The chatbot provides clear, structured answers about program details including admissions, courses, tuition, internships, and more.

---

### 🎯 Project Goal

The goal of this assistant is to:
- Provide fast and accurate responses to common inquiries about the AI Master's program.
- Automate the registration interest process by collecting basic user information.
- Handle user inputs gracefully, even when questions are unrelated or incomplete.

---

### 🔍 Core Features

- **Intent Recognition**: Understands user queries such as "How long is the program?" or "Do you offer internships?" using machine learning classifiers.
- **Entity Extraction**: Identifies key data like names, emails, and course names from user input.
- **Slots**: Stores extracted values (e.g., `first_name`, `email`) and uses them to personalize replies and manage context.
- **Forms**: Collects required information (like first name and email) interactively to complete the registration interest form.
- **Fallback Handling**: Uses confidence thresholds to catch unclear or out-of-scope questions and respond accordingly.

---

### 🧠 Training and Techniques Used

The assistant is trained using a custom Rasa NLU pipeline, combining classical NLP techniques with deep learning models:

```yaml
pipeline:
  - name: SpacyNLP
    model: "en_core_web_sm"
  - name: SpacyTokenizer
  - name: SpacyFeaturizer
  - name: CountVectorsFeaturizer
  - name: DIETClassifier
    epochs: 100
  - name: RegexEntityExtractor
  - name: CRFEntityExtractor
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100
  - name: FallbackClassifier
    threshold: 0.4
    ambiguity_threshold: 0.1


### 🔌 Integrations

This chatbot is integrated with two key communication channels to ensure wide accessibility and real-time interaction:

#### ✅ Twilio WhatsApp Integration
The assistant is connected to WhatsApp via Twilio, allowing users to chat directly with the bot through their mobile devices. This provides a convenient and instant messaging experience for prospective students who prefer using WhatsApp.

- Real-time messaging
- Message delivery reports
- WhatsApp-approved chatbot compliance

#### ✅ Web Chat Widget using Socket.IO
A custom web-based chat widget is embedded on the university's website using `rasa-webchat`, which communicates with the bot via `Socket.IO`. This allows students to ask questions directly through the site without needing any external app.

- Lightweight and responsive widget
- Real-time communication with the Rasa backend
- Customizable UI and branding

These integrations ensure the assistant is available both on mobile and desktop platforms, improving accessibility and user engagement.
