import React, {Component} from 'react';

import WorkSpace from './WorkSpace';
import Advertisment from './Advertisment';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      data: null
    };

    this.fetchNewProblemSet = this.fetchNewProblemSet.bind(this);
    this.fetchSubsequentProblemSet = this.fetchSubsequentProblemSet.bind(this);
  }
  componentDidMount() {
    this.fetchNewProblemSet()
  };

  fetchNewProblemSet() {
    var url = "http://localhost:5000/api/problem_set_generator/5/2"
    fetch(url, {
      mode: "cors"
    })
      .then(res => res.json())
      .then(
          (result) => {
          this.setState({
            isLoaded: true,
            data: JSON.parse(result)
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
    };

  fetchSubsequentProblemSet() {
    this.setState({
      error: null,
      isLoaded: false,
      data: null
    });
    this.fetchNewProblemSet()
  };


  render() {
    const { error, isLoaded, data } = this.state;
    if (error) {
      return <div>{error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading</div>;
    } else if (data) {
      return (
        <div className='container'>
            <WorkSpace
            problems={this.state.data.problems}
            fetchSubsequentProblemSet={this.fetchSubsequentProblemSet}
            />
        </div>
      );
    }
  }
}

export default App;

// API response is of the form:
//
//    {'grades': [.92, .5]
//     'graded': False,
//     'problems': [
//         {'question': '', 'answer':'', 'difficulty': 0, 'result':True},
//         {'question': '', 'answer':'', 'difficulty': 0, 'result':False},
//         {'question': '', 'answer':'', 'difficulty': 1, 'result':False}
//         ],
//     }
