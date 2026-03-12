import { useState, useRef, useEffect } from 'react';
import { sendChatMessage } from '../services/api';

export default function Chatbot() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState([
    { role: 'bot', text: 'Namaste! 🙏 I\'m your India travel assistant. Ask me anything about travel in India!' },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEnd = useRef(null);

  useEffect(() => {
    messagesEnd.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async () => {
    const text = input.trim();
    if (!text || loading) return;

    setMessages(prev => [...prev, { role: 'user', text }]);
    setInput('');
    setLoading(true);

    try {
      const data = await sendChatMessage(text);
      setMessages(prev => [...prev, { role: 'bot', text: data.reply }]);
    } catch {
      setMessages(prev => [...prev, {
        role: 'bot',
        text: 'Sorry, I couldn\'t process that. Please try again!'
      }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <>
      <button
        className="chatbot-toggle"
        onClick={() => setOpen(!open)}
        aria-label="Toggle chatbot"
        id="chatbot-toggle"
      >
        {open ? '✕' : '💬'}
      </button>

      {open && (
        <div className="chatbot-window" id="chatbot-window">
          <div className="chatbot-header">
            <span className="chatbot-header-title">🇮🇳 Travel Assistant</span>
            <button className="chatbot-close" onClick={() => setOpen(false)}>✕</button>
          </div>

          <div className="chatbot-messages">
            {messages.map((msg, i) => (
              <div key={i} className={`chat-message ${msg.role}`}>
                {msg.text}
              </div>
            ))}
            {loading && (
              <div className="chat-message bot">
                <em>Thinking...</em>
              </div>
            )}
            <div ref={messagesEnd} />
          </div>

          <div className="chatbot-input-area">
            <input
              className="chatbot-input"
              type="text"
              placeholder="Ask about travel in India..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              id="chatbot-input"
            />
            <button
              className="chatbot-send"
              onClick={handleSend}
              disabled={loading}
              id="chatbot-send"
            >
              ➤
            </button>
          </div>
        </div>
      )}
    </>
  );
}
