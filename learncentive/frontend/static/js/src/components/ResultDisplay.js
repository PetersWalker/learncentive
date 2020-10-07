import React, {Component} from 'react'

class ResultDisplay extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return(<div className='container'>{this.props.answer_status}</div>)
  }
}

export default ResultDisplay;
