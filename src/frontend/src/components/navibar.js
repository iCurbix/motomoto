import React, {Component} from 'react';
import {FormControl, Form, Navbar, Button, Nav} from "react-bootstrap";
import Navibaruser from "./navibaruser";
import {Link} from "react-router-dom";

class Navibar extends Component {
    constructor(props) {
        super(props);

        this.state = {
            isLoggedIn: true,
            username: 'iCurbix'
        };

        this.logout = this.logout.bind(this)
    }

    logout() {
        this.setState({isLoggedIn: false})
    }

    render() {
        return (
            <div>
            <Navbar bg={'dark'} variant={'dark'} sticky={'top'}>
                <Link to={'/'}>
                    <Navbar.Brand>motomoto</Navbar.Brand>
                </Link>
                <Form inline className={'mr-auto'}>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Link to={'/search'}>
                        <Button variant="outline-info">Search</Button>
                    </Link>
                </Form>
                <Nav>
                    <Navibaruser isLoggedIn={this.state.isLoggedIn} username={this.state.username} logoutHandler={this.logout}/>
                </Nav>
            </Navbar>
            </div>
        );
    }
}

export default Navibar;