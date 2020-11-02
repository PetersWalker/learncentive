import React, {Component} from 'react';

import ProblemDisplay from './ProblemDisplay';
import InputForm from './InputForm';
import ResultDisplay from './ResultDisplay';

class WorkSpace extends Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 0,
      answer_status: null
    };
    this.handleAnswerSubmission = this.handleAnswerSubmission.bind(this);
  }

  handleAnswerSubmission(value) {
    if (this.state.counter == (this.props.problems.length - 1)) {
      this.props.fetchSubsequentProblemSet()
      this.setState({counter: 0})
    } else {
      if (this.props.problems[this.state.counter]['answer'] == value) {
        this.setState({
          answer_status: 'correct'
        });
        this.props.problems[this.state.counter]['correct'] = true;
      } else { this.setState({answer_status: 'wrong'}) }

      this.setState({ counter: this.state.counter + 1})
    }
  }


  render() {
      return(
          <div className="workspace">
            <ProblemDisplay counter={this.state.counter} problems={this.props.problems}/>
            <ResultDisplay answer_status={this.state.answer_status}/>
            <InputForm handleAnswerSubmission={this.handleAnswerSubmission}/>
          </div>
      );
  }
}

export default WorkSpace;
