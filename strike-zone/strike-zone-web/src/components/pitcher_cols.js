import React from 'react'

import {Card} from './card.js'

export class PitcherCols extends React.Component{
    constructor(props){
        super(props)
        console.log("CHEESE");
        console.log(this.props.players)

        this.generateRows = this.generateRows.bind(this);
    }

    generateRows(_ply, rowIndex){
        return (
            <tr>
                <Card player={_ply} type={"player"}/>
            </tr>
            
        );
    }

    render() {
        
        return (
            <div className="division">
                <table>
                    <thead className="division-head"><tr><th>{this.props.name}</th></tr></thead>
                    <tbody className="division-body">{this.props && this.props.players && this.props.players.map(this.generateRows)}</tbody>
                </table>
            </div>
        );
    }
}