import React, {Component} from 'react';

class ProblemDisplay extends Component {

  render() {
      return (
        <>
          <h1>{this.props.problems[this.props.counter]['question']}</h1>
        </>
        );
    }
  }

export default ProblemDisplay;
