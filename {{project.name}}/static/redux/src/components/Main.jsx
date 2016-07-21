import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'


class Main extends Component {

  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
	Main
      </div>
    )
  }

}

export default connect()(Main)
