import React, {Component} from 'react';

class ProblemDisplay extends Component {

  render() {
      return (
        <>
          <h1>{this.props.problems[this.props.counter]['question']}</h1>
          <h2>{this.props.counter}</h2>
        </>
        );
    }
  }

export default ProblemDisplay;
