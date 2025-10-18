# SafeSpeak: Real-Time Cyberbullying Detection Before Posting

A comprehensive applied machine learning and deep learning project to detect cyberbullying in social media text **before** it gets posted.

## 🚀 Overview

Cyberbullying remains a major challenge on online platforms, often causing psychological harm before it can be removed. **SafeSpeak** offers a real-time detection system leveraging both classic ML and modern BERT models, with a friendly GUI for instant pre-posting intervention.

- **Domain:** Natural Language Processing, Social Media Moderation
- **Tech:** Python, Jupyter, Scikit-learn, Transformers, Tkinter

## 📊 Datasets & Pretrained Models

- Over **57,000** annotated comments from Twitter, YouTube, Kaggle
- All preprocessed datasets and trained model files:
  - [Google Drive: Models & Datasets](https://drive.google.com/drive/folders/1HVStB0s8n0f7ZbYmip0JAI-rJTlgu1pm)

## ⚙️ How to Run

1. **Clone the repository**
git clone https://github.com/Suke712/Cyberbullying-Detection.git
cd Cyberbullying-Detection

2. **Download models/datasets**  
Download from the [Google Drive folder](https://drive.google.com/drive/folders/1HVStB0s8n0f7ZbYmip0JAI-rJTlgu1pm) and place in the project directory.

3. **Run Jupyter Notebooks**  
- View/modify code, run cell-by-cell
- _Dependencies:_ See each `.ipynb` for library installs

4. **Try the Safe Keyboard (GUI)**  
- Open the attached notebook/script with Tkinter GUI for live demo

## 🧠 Main Features

- **Pre-trained BERT & classic ML support:** Evaluate and compare
- **Robust preprocessing:** Emojis, URLs, slang, label noise handling
- **Instant Feedback GUI:** Prototype “Safe Keyboard” warns users before posting
- **Well-commented code:** For learning and research extension

## 📊 Results

| Model            | Accuracy | F1-Score | Inference Time |
|------------------|----------|----------|---------------|
| BERT             | 0.84     | 0.83     | ~200ms        |
| Linear SVC (TFIDF) | 0.80     | 0.79     | ~35ms         |
| Logistic Regression      | 0.78     | 0.77     | ~30ms         |
| Naive Bayes      | 0.72     | 0.72     | ~25ms         |

## 📜 Research

- [Applied Research Paper](./SafeSpeak%28Applied%20Research%20Paper%29.pdf)
- [Presentation Slides (PDF)](./SafeSpeak%28PPT%29.pdf)

## 🙏 Credits

- Data sources: Twitter, YouTube, Kaggle ([original dataset link](https://www.kaggle.com/datasets/saurabhshahane/cyberbullying-dataset))
- Inspired by recent research and community efforts to promote civility online.

---

> **Note:** For custom training or use with new data, adjust and retrain using the provided notebooks.

---

**Feel free to fork, open issues, or submit PRs for improvements!**


