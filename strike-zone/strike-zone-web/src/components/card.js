import React from 'react'
import {Link} from 'react-router-dom'

import './main.css'
import logo from '../images/softball.png'

export class Card extends React.Component {

    constructor(props) {
        super(props);

        this.state = {

        }

        this.playerCard = this.playerCard.bind(this);
    }

    playerCard() {
        if (this.props.type === "player"){
            let link = `/player/${this.props.player.ID}`
            return(
                <Link class="card" to={{pathname: link, state:{id: this.props.player.ID, name: this.props.player.name}}}>
                    <p>PL</p>
                    <h2 class="card-name">{this.props.player.name}</h2>
                </Link>
            )
        }
        else{
            let link = `/team/${this.props.name[1]}`
            return(
                <Link class="card" to={{pathname: link, state:{team: this.props.name[1]}}}>
                    <img class="card-image" src={logo} />
                    <h2 class="card-name">{this.props.name[0]}</h2>
                </Link>
            )
            
        }
    }
    render() {

        
        return (
            
            <td>
                {this.playerCard()}
            </td>            
            
        );
    }
}