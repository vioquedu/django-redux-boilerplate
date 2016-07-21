import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import {Row, Col } from 'react-bootstrap'

class Account extends Component {

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
	<Row>
	  <Col md={3}>
	  </Col>
	  <Col md={3}>
	    Hola account
	  </Col>

	</Row>
      </div>
    );
  }
}

export default connect()(Account)
