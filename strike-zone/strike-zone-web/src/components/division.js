import React from 'react'
import {Card} from './card.js'
import './main.css'

export class Division extends React.Component {
    constructor(props) {
        super(props);
        console.log("OI")
        console.log(this.props.teams)
    
        this.generateRows = this.generateRows.bind(this);
    }

    generateRows(_name, rowIndex){

        return (
            <tr>
                <Card name={_name} type={"team"}/>
            </tr>
            
        );
    }

    render() {
        var teams = this.props.teams
        
        
        return (
            <div className="division">
                <table>
                    <thead className="division-head"><tr><th>{this.props.name}</th></tr></thead>
                    <tbody className="division-body">{this.props && this.props.teams && this.props.teams.map(this.generateRows)}</tbody>
                </table>
            </div>
        );
    }
}