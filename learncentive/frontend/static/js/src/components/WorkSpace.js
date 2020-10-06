import React, {Component} from 'react';

import ProblemDisplay from './ProblemDisplay'
import InputForm from './InputForm'

class WorkSpace extends Component {
  render() {
      return(
        <div>
          <h1>Workspace</h1>
          <ProblemDisplay />
          <InputForm />
        </div>
      );
  }
}

export default WorkSpace;
