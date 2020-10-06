import React, {Component} from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

class InputForm extends Component {

  render() {
    return(
      <div>
      <Form>
        <Form.Group>
          <Form.Label>Answer</Form.Label >
          <Form.Control type="string" placeholder="Type Answer"/>
        </Form.Group>
        <Form.Group>
          <Button variant="primary" type="submit">
            Enter
          </Button>
        </Form.Group>
      </Form>
      </div>
    )
  }
}

export default InputForm;
