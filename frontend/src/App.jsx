import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [file, setFile] = useState(null);
  const [uploadMessage, setUploadMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadPDF = async () => {
    if (!file) {
      setUploadMessage("Please select a PDF first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setUploadMessage("Uploading and processing...");

      const response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (response.ok) {
        setUploadMessage("✓ PDF processed successfully");
      } else {
        setUploadMessage("Upload failed.");
      }
    } catch (error) {
      setUploadMessage("Unable to connect to backend.");
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: question,
          }),
        }
      );

      const data = await response.json();

      if (response.ok) {
        setAnswer(data.answer);
      } else {
        setAnswer("Something went wrong.");
      }
    } catch (error) {
      setAnswer("Unable to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-logo">F</div>
          <div>
            <div className="brand-name">FinAI</div>
            <div className="brand-subtitle">Document Intelligence</div>
          </div>
        </div>

        <nav className="navigation">
          <div className="nav-item active">
            <span>Dashboard</span>
          </div>

          <div className="nav-item">
            <span>Documents</span>
          </div>

          <div className="nav-item">
            <span>AI Assistant</span>
          </div>
        </nav>

        <div className="sidebar-bottom">
          <div className="status-dot"></div>
          <div>
            <strong>AI Ready</strong>
            <small>Document assistant online</small>
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="main-content">

        <header className="topbar">
          <div>
            <p className="eyebrow">AI FINANCIAL ANALYSIS</p>
            <h1>Financial Document Summarizer</h1>
            <p className="subtitle">
              Upload a financial document and ask questions using AI.
            </p>
          </div>

          <div className="system-status">
            <span className="status-dot"></span>
            System Ready
          </div>
        </header>

        <section className="dashboard-grid">

          {/* UPLOAD CARD */}
          <div className="card upload-card">
            <div className="card-label">DOCUMENT</div>

            <h2>Upload your report</h2>

            <p className="card-description">
              Upload an annual report, financial statement or other PDF.
            </p>

            <div className="upload-box">
              <div className="upload-icon">↑</div>

              <h3>Choose a PDF document</h3>

              <p>
                {file
                  ? file.name
                  : "Drag and drop your file here or browse"}
              </p>

              <input
                id="pdf-upload"
                type="file"
                accept=".pdf"
                onChange={(e) => setFile(e.target.files[0])}
              />

              <label htmlFor="pdf-upload" className="browse-button">
                Browse files
              </label>
            </div>

            <button
              className="primary-button"
              onClick={uploadPDF}
            >
              Upload & Process
            </button>

            {uploadMessage && (
              <p className="upload-message">{uploadMessage}</p>
            )}
          </div>

          {/* HOW IT WORKS */}
          <div className="card process-card">
            <div className="card-label">HOW IT WORKS</div>

            <h2>Analyze documents with AI</h2>

            <div className="steps">

              <div className="step">
                <div className="step-number">01</div>
                <div>
                  <h3>Upload</h3>
                  <p>Upload your financial PDF.</p>
                </div>
              </div>

              <div className="step">
                <div className="step-number">02</div>
                <div>
                  <h3>Process</h3>
                  <p>Relevant document content is retrieved.</p>
                </div>
              </div>

              <div className="step">
                <div className="step-number">03</div>
                <div>
                  <h3>Ask AI</h3>
                  <p>Ask questions and get document-based answers.</p>
                </div>
              </div>

            </div>
          </div>

        </section>

        {/* AI ASSISTANT */}
        <section className="card assistant-card">

          <div className="card-label">AI ASSISTANT</div>

          <h2>Ask about your document</h2>

          <p className="card-description">
            Ask a question based on the information in your uploaded PDF.
          </p>

          <div className="question-area">
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Example: What was the company's revenue in 2025?"
            />

            <button
              className="ask-button"
              onClick={askQuestion}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "Ask AI"}
            </button>
          </div>

          {loading && (
            <div className="loading-box">
              <div className="spinner"></div>
              <span>AI is analyzing your document...</span>
            </div>
          )}

          {answer && !loading && (
            <div className="answer-section">
              <div className="answer-header">
                <span className="ai-badge">AI</span>
                <strong>Answer</strong>
              </div>

              <div className="answer-box">
                {answer}
              </div>
            </div>
          )}

        </section>

        <footer>
          <span>FinAI</span>
          <span>AI-assisted financial document analysis</span>
        </footer>

      </main>
    </div>
  );
}

export default App;