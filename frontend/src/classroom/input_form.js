import React from 'react'

class InputForm extends React.Component {
  constructor(props){
    super(props);
    this.state = {value:''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    this.props.buttonHandler(this.state.value);
    event.preventDefault();


    //TODO clear form
    // clear state
  }

  handleChange(event) {
    this.setState({
      value: event.target.value
    });
  }

  render() {
    return(
      <form onSubmit={this.handleSubmit}>
        <label>
          Answer:
          <input type="text" value={this.state.value}
          onChange={this.handleChange}/>
        </label>
        <input type="submit" value="Submit"/>
      </form>
    )
  }
}

export default InputForm
