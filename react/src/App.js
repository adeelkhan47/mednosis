import { useState } from 'react';
import './App.css';
import { Footer } from './Footer';
import config from "./config.json";
import axios from 'axios';


function App() {
  const question_placeholder = "Ask away!";
  const [questionVal, setQuestionVal] = useState("I feel pain in my legs and dizziness, what should I do?");
  const [question, setQuestion] = useState();
  const [questionPlaceholder, setQuestionPlaceholder] = useState(question_placeholder);
  const [answer, setAnswer] = useState();
  const [error, setError] = useState();
  const ask = async () => { 
    if (!questionVal)
      return;
    setQuestion(questionVal); 
    setQuestionVal("");
    setAnswer("");
    setError("");
    setQuestionPlaceholder("Loading...");
    await axios.post(
      config.BASE_URL + "gpt", 
      { "prompt": questionVal }
    ).then(response => {
      console.log(response);
      setQuestionPlaceholder(question_placeholder);
      if (response.status === 200) {
        setQuestionVal(response.data.question);
        console.log(response.data.data)
        setAnswer(response.data.data);
      } else {
        setError("Unusual, try again!");
      }
    }).catch(e => {
      let response = e.response;
      if (response?.status === 400) {
        setQuestionVal(response.data.question);
        setError(response.data.error);
      } else {
        setError("Unusual, try again!");
      }
    });
  }
  return (
    <div>
      <div className="header">
          <div className="content">
              <h1>MedNosis</h1>
              <p>AI Medical Advice</p>
          </div>
      </div>
      <div className="page-wrap">
        <div className="page-content clearfix">
            <div className="inner-head">
                <h1 className="heading">Hi! I'm your AI doctor! 👨🏻‍⚕️ 🩺 I'm happy to help you! 🏥 💊</h1>
                <textarea 
                  className={"question" + (question && !answer && !error ? " loading" : "")} 
                  onChange={e => setQuestionVal(e.target.value)} 
                  placeholder={questionPlaceholder} 
                  value={questionVal}
                ></textarea>
                {
                  question && !answer && !error ? "" :
                  <button className="ask-button" onClick={ask}>
                    <i className="fa-solid fa-heart-circle-bolt"></i>
                  </button>
                }
            </div>
            <div className={error ? "message red" : ""}>
              {error}
            </div>
            <div className="float-left">
              <div className={question && answer ? "card-question" : ""}>
                {answer && question ? question : ""}
              </div>
            </div>
            <div className="float-left">
              <div 
                className={answer ? "card-reply" : ""} 
                dangerouslySetInnerHTML={{ __html: answer }}
              >
              </div>
            </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default App;
