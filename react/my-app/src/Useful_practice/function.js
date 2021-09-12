import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';


function Welcome(props){
  return <h1>Hello, {props.name}</h1>
}

function App2(){
  return (
    <div>
      <Welcome name = "aa"></Welcome>
      <Welcome name = "ee"></Welcome>

    </div>
  )
}

ReactDOM.render(
  <App2></App2>,
  document.getElementById('root')
)
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
