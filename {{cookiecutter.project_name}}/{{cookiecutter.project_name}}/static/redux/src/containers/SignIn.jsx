import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { Row, Col, Panel, FormGroup, ControlLabel, FormControl,
Button, Alert } from 'react-bootstrap'
import { update_login_form, loginUser } from '../actions/auth_actions'

class SignIn extends Component {

  constructor(props) {
    super(props)
  }

  
  handleForm(event) {
    // Handle form submission
    // Firs prevent direct submission
    event.preventDefault();
    const { dispatch } = this.props
    dispatch(loginUser({
      username: this.props.username, 
      password: this.props.password
    }));
  }

  updateLoginForm(event, key) {
    // Function used to update login form as user types.
    const { dispatch } = this.props
    dispatch(update_login_form(event.target.value, key))
  }

  render() {
    // Panel title
    const title = (<h4>Sign in</h4>);

    // Show errors if availables.
    var error = undefined
    if(this.props.error != null ) {
      error = (
	<Alert bsStyle="danger" >
	  Login was not possible with provided credentials.
	</Alert>
      );
    } 
      

    return (
      <div>	
	<Row>
	  <Col md={4} mdOffset={4}>
	    {error}
	    <Panel header={title} >
	      <form onSubmit={(event) => this.handleForm(event)}>
		<FormGroup >
		  <ControlLabel>User name</ControlLabel>
		  <FormControl 
		      onChange={(event) => this.updateLoginForm(event, 'username')}
		      value={this.props.username}
		      type="text" />
		  <br/>
		  <ControlLabel>Password</ControlLabel>
		  <FormControl 
		      onChange={(event) => this.updateLoginForm(event, 'password')}
		      value={this.props.password}
		      type="password" />
		</FormGroup>
		<Button bsStyle="primary"
			type="submit"
			onClick={(event) => this.handleForm(event)}
		>Submit</Button>
	      </form>
	    </Panel>
	  </Col>
	</Row>
      </div>
    )
  }
}

SignIn.propTypes = {
  username: PropTypes.string,
  password: PropTypes.string,
  error: PropTypes.object
}

function mapStateProps(state, ownProps) {
  const { auth } = state
  const { login_form, error } = auth
  return {
    username: login_form.username,
    password: login_form.password,
    error: error
  }
}

export default connect(mapStateProps)(SignIn)
