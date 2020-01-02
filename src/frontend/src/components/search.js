import React, {Component} from 'react';
import axios from 'axios';

class Search extends Component {

    constructor(props) {
        super(props);

        this.state = {
            productList: []
        }
    }

    componentDidMount() {
        axios.get('http://localhost:5000/asdf', {
            headers: {
               // 'Access-Control-Allow-Origin': '*',
            }
        })
            .then(response => {
                console.log(response);
                this.setState({productList: response})
            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        return (
            <div>
                search
            </div>
        );
    }
}

export default Search;