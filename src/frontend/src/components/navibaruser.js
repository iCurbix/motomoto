import React from 'react';
import {Nav, NavDropdown} from 'react-bootstrap';

function Navibaruser(props) {
    return props.isLoggedIn ? (
        <NavDropdown title={props.username} id="collasible-nav-dropdown" alignRight>
            <NavDropdown.Item href="#">Price alerts</NavDropdown.Item>
            <NavDropdown.Item href="#">Account</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item onClick={props.logoutHandler}>Logout</NavDropdown.Item>
        </NavDropdown>
    ) : (
        <Nav.Link href={'#'}>Log in</Nav.Link>
    );
}

export default Navibaruser;