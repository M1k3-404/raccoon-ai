"use client"

import { Input, NextUIProvider, ScrollShadow, Button } from "@nextui-org/react";
import Question from "./ui/Conversation/question";
import Response from "./ui/Conversation/response";
import { FiPause, FiPlus } from "react-icons/fi";
import { useState } from "react";
import axios from "axios";
import ResponseLoading from "./ui/Conversation/responseLoading";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [questionsList, setQuestionsList] = useState([]);
  const [isGenerating, setIsGenerating] = useState(false);

  {/* Display question component and access backend API */}
  const addQuestion = () => {
    if (!question.trim()) {
      return;
    }

    setIsGenerating(true);

    const questionObject = {
      question,
      response: null
    }

    setQuestionsList([...questionsList, questionObject]);
    setQuestion("");

    generateResponse(questionObject);
  }

  const generateResponse = async (questionObject) => {
    try {
      const response = await axios.post("http://localhost:5000/generate_prompt", {
        prompt: questionObject.question
      })

      setQuestionsList([...questionsList, { ...questionObject, response: response.data.response }]);
    } catch (error) {
      if (error.response) {
        if (error.response.status === 500) {
          console.log("Error Response: ", error.response.data);
          setQuestionsList([...questionsList, { ...questionObject, response: error.response.data.error }]);
        } else {
          console.log("Error generating response.");
          setQuestionsList([...questionsList, { ...questionObject, response: "Sorry, an unknown error occurred." }]);
        }
      } else if (error.request) {
        console.log("No response recieved from server.");
        setQuestionsList([...questionsList, { ...questionObject, response: "Sorry, an error occurred. No response received from server. Please check your internet connection and try again" }]);
      } else {
        console.log("Error setting up the request:", error.message);
      setQuestionsList([...questionsList, { ...questionObject, response: "An error occurred while setting up the request. Please try again later" }]);
      }      
    } finally {
      setIsGenerating(false);
    }
  }

  return (
    <NextUIProvider className="w-full h-full">
      <main className="flex w-full h-full flex-col items-center justify-end">
        <ScrollShadow size={10} hideScrollBar className="w-[96%] h-[85%] flex flex-col mx-auto">
          {questionsList.map((question, index) => (
            <div key={index} className="flex flex-col">
              <Question question={question.question} />
              { isGenerating ? <ResponseLoading /> : <Response id={index} prompt={question.question} response={question.response} /> }
            </div>
          ))}
        </ScrollShadow>
        <div className="w-[96%] h-[10%] flex flex-row justify-evenly mx-auto">
          <Input 
            type="text"
            size="lg"
            className="w-[92%] self-center"
            placeholder="Ask Rocket..." 
            isDisabled={isGenerating}
            value={question} 
            onChange={(e) => setQuestion(e.target.value)} 
          />
          <Button 
            size="lg" 
            className="aspect-square rounded-2xl border-2 bg-transparent border-white text-white self-center" 
            isDisabled={isGenerating}
            onClick={addQuestion}
          >
            { isGenerating ? <FiPause /> : <FiPlus /> }
          </Button>
        </div>
      </main>
    </NextUIProvider>
  );
}
