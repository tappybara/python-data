import React from 'react'
import './main.css'
import logo from '../images/softball.png'

export class Card extends React.Component {

    constructor(props) {
        super(props);

        this.state = {

        }
    }
    render() {
        return (
            <div class="card">
                <img class="card-image" src={logo} />
                <h2 class="card-name">Toronto Blue Jays</h2>
            </div>
        );
    }
}