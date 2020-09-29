import React from 'react'

import InputForm from './input_form'

class ProblemContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state =  {
      problem_set: null,
      correct_answer: null,
      question: null,
      error: undefined,
    };
    this.buttonHandler = this.buttonHandler.bind(this)
    this.counter = 0
  }

  componentDidMount() {
    this.getProblemSet();
    console.log(this.state.problem_set)
  }

  componentUpdate() {
    //this.setCounterAndAnswer();

  }

  getProblemSet() {
    fetch("http://localhost:5000/api/problem_set_generator/10/0")
      .then(response => response.json())
      .then((data) => {this.setState({
        problem_set: data,
        question: data['problem'][this.counter]['question'],
        correct_answer: data['problem'][this.counter]['answer']
      })})
      .catch(error => {
        console.log(error);
        this.setState({
          error: error
        })
      });
  }

  buttonHandler(submitted_answer) {

    console.log('submitted:', submitted_answer);
    console.log('correct:', this.state.correct_answer);
    console.log('counter:', this.state.counter);


    if (submitted_answer === this.state.correct_answer){
      alert('YOU ARE CORRECT')
    } else if (submitted_answer !== this.state.correct_answer){
      alert('WRONG')
    } else console.log('dammit');
    this.setCounterAndAnswer()
  }

  setCounterAndAnswer(counter) {
    if (this.state.problem_set) {
      if (this.counter === 4) {
        this.getProblemSet()
      } else {
        this.counter = this.counter + 1;
        this.setState(prevState => {
          return {
            correct_answer: this.state.problem_set[this.counter]['answer']
          }
        })
      }
    };
  }

  displayProblem() {

    if (this.state.problem_set) {
      return(this.state.problem_set[this.counter]['question'])
    } else {
      return(null)
    }
  }
  //{this.setCounterAndAnswer()}

  render() {
        return(
      <div>
        <h1>
          {this.displayProblem()}
        </h1>
        <InputForm
          buttonHandler={this.buttonHandler}
          key='buttonHandler'
          />
          {this.counter}
      </div>

    )
  }

}

// console.log('AFTER FUNCTION');
// console.log('correct:', this.state.correct_answer);
// console.log('counter:', this.state.counter);


export default ProblemContainer
