import React, { useState } from 'react';
import {Route, Routes, Link} from "react-router-dom"
import { Result } from './pages/Result';

export default function App() {
	const questions = [
		{
			questionText: 'After washing your face with a cleanser, describe how your face feels after 5 minutes:',
			answerOptions: [
				{ answerText: 'Flakey/Tight throughout the face', answer: "Dry" },
				{ answerText: 'Shiny throughout the face', answer: "Oily" },
				{ answerText: 'Shiny only on your my T-Zone (chin, nose, forehead)', answer: "Combination" },
				{ answerText: 'Hydrated or comfortable', answer: "Normal" },
			],
		},
		// {
		// 	questionText: 'After a long day, my skin is:',
		// 	answerOptions: [
		// 		{ answerText: 'Shiny', answer: "Dry" },
		// 		{ answerText: 'Shiny only on my T-Zone', answer: "Oily" },
		// 		{ answerText: 'Red, flakey and tight', answer: "Combination" },
		// 		{ answerText: 'Looks the same as it did when I left the house this morning', answer: "Normal" },
		// 	],
		// },
		{
			questionText: 'What is your main skin concern?',
			answerOptions: [
				{ answerText: 'Acne',answer: 'Acne'},
        { answerText: 'Aging', answer: 'Aging'},
        { answerText: 'Blackheads', answer: 'Blackheads'},
        { answerText: 'Dark Circles', answer: 'Dark Circles'},
        { answerText: 'Dullness', answer: 'Dullness'},
        { answerText: 'Pores', answer: 'Pores'},
        { answerText: 'Redness', answer: 'Redness'},
        { answerText: 'Sensitivity', answer: 'Sensitivity'},
        { answerText: 'Sun Damage', answer: 'Sun Damage'},
        { answerText: 'Uneven Skintone', answer: 'Uneven Skintone'}
			],
		}
	];

	const [currentQuestion, setCurrentQuestion] = useState(0);
	const [showScore, setShowScore] = useState(false);
	const [score, setScore] = useState(0);
  const [array, setData] = useState([]);
  // var array=[];

	const handleAnswerOptionClick = (answer) => {
		// if (isCorrect) {
		// 	setScore(score + 1);
		// }
    setData(array => [...array, answer]);

		const nextQuestion = currentQuestion + 1;
		if (nextQuestion < questions.length) {
			setCurrentQuestion(nextQuestion);
		} else {
			setShowScore(true);
		}
	};

  const changeRoute = () =>{

  };

	return (
    <div className='body'>
      <h1 className='title'>
            <font color="#fc9790">S</font>
            <font color="#7fa367">n</font>
            <font color="#9a77b5">a</font>
            <font color="#65ccf7">i</font>
            <font color="#f0c94a">l</font>
            <font color="#98fa7d">C</font>
            <font color="#66CC66">a</font>
            <font color="#FF9966">r</font>
            <font color="#FFCCCC">e</font>
        </h1>
		<div className='app'>
			
      {showScore ? (
        <>
        <Routes>
          <Route path="/Result" element={<Result />} />
        </Routes>
				<div className='score-section'>
          Your Skin Profile:
					<ul>
          {array.map((answers) => (
            <li>{answers}</li>
          ))}
        </ul>
        <button className="Results"><a href="http://127.0.0.1:5500/react-flask-app/src/pages/result.html">Check out your routine!</a></button>
				</div>
        </>  
			) : (
				<>
					<div className='question-section'>
						<div className='question-count'>
							<span>Question {currentQuestion + 1}</span>/{questions.length}
						</div>
						<div className='question-text'>{questions[currentQuestion].questionText}</div>
					</div>
					<div className='answer-section'>
						{questions[currentQuestion].answerOptions.map((answerOption) => (
							<button onClick={() => handleAnswerOptionClick(answerOption.answer)}>{answerOption.answerText}</button>
						))}
					</div>
				</>
			)}
		</div>
    </div>
	);
}