import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'

class Logout extends Component {

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
	Logout successfully
      </div>
    );
  }
}

export default connect()(Logout)
