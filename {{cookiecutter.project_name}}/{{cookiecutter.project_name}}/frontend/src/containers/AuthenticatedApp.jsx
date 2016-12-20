import React, { Component, PropTypes } from 'react'
import { LinkContainer } from 'react-router-bootstrap'
import $ from 'jquery'
import idle from 'jquery.idle'
import { connect } from 'react-redux'
import { Link, browserHistory } from 'react-router'
import { resetErrorMessage } from '../actions'
import { Grid, Navbar, Nav, NavItem } from 'react-bootstrap';
import { logoutUser } from '../actions/auth_actions'

class AuthenticatedApp extends Component {

  constructor(props) {
    super(props)
  }

  componentDidMount() {
    $(document).idle({
      onIdle: this._onIdle.bind(this),
      idle: 5000*60
    }, this)
      
  }
  _onIdle() {
    console.log('Hola')
    const { isAuthenticated } = this.props
    if(isAuthenticated) {
      this.logout()
    }
  }

  logout() {
    // Logout user
    const { dispatch } = this.props;
    dispatch(logoutUser())
  }

  get navbar() {
    const { isAuthenticated, payload } = this.props

    if(isAuthenticated) {
      var right_icons = (
	<Nav pullRight>
	<NavItem eventKey={2} >
	{payload.username.toUpperCase()}
	</NavItem>
	<NavItem eventKey={1} 
	onClick={(event) => this.logout()}>
	Logout
	  </NavItem>	    
	</Nav>
      );      
    } else {
      var right_icons = (
	<Nav pullRight>
	  <LinkContainer to="/signin/">
	    <NavItem eventKey={1}>
	      Sign in
	    </NavItem>	    
	  </LinkContainer>
	</Nav>
      );      
    }

    return (
      <Navbar fluid={true}>
	<Navbar.Header>
	  <Navbar.Brand>
	    <Link to="/">
	{{cookiecutter.project_name}}
	    </Link>
	  </Navbar.Brand>
	</Navbar.Header>
	<Nav>
	</Nav>
	{right_icons}
      </Navbar>
    )
  }


  render() {


    return (
      <div>
	{this.navbar}
	<br/>
	<Grid fluid={true}>	  
	  {this.props.children}
	</Grid>
      </div>
    )
  }
}

AuthenticatedApp.propTypes = {
  isAuthenticated: PropTypes.bool,
  payload: PropTypes.object
}

function mapStateToProps(state, ownProps) {
  const { auth } = state
  const { isAuthenticated, payload } = auth
  return {
    isAuthenticated: isAuthenticated,
    payload: payload
  }
}

export default connect(mapStateToProps)(AuthenticatedApp)
