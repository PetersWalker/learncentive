import React, {Component} from 'react';

import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

import WorkSpace from './WorkSpace';
import Advertisment from './Advertisment';

class App extends Component {
  render() {
    return(
          <div>
          <Container/>
            <Row>
              <Col><WorkSpace /></Col>
              <Col><Advertisment /></Col>
            </Row>
          <Container />
          </div>

    );
  }
}

export default App;
