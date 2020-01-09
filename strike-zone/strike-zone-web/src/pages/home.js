import React from 'react';

import './page.scss'
import {Division} from '../components/division.js'


export class Home extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            al_east: [["Baltimore Orioles", "BAL"], ["Boston Red Sox","BOS"], ["New York Yankees", "NYY"], ["Tampa Bay Rays", "TB"], ["Toronto Blue Jays", "TOR"]],
            al_west: [["Houston Astros", "HOU"], ["Los Angeles Angels","LAA"], ["Oakland Athletics", "OAK"], ["Seattle Mariners", "SEA"], ["Texas Rangers", "TEX"]],
            al_central: [["Chicago White Sox", "CWS"], ["Cleveland Indians", "CLE"], ["Detroit Tigers", "DET"], ["Kansas City Royals", "KC"], ["Minnesota Twins", "MIN"]],
            nl_east: [["Atlanta Braves", "ATL"], ["Miami Marlins", "MIA"], ["New York Mets", "NYM"], ["Philadelphia Phillies", "PHI"], ["Washington Nationals", "WSH"]],
            nl_west: [["Arizona Diamondbacks", "ARI"], ["Colorado Rockies", "COL"], ["Los Angeles Dodgers", "LAD"], ["San Diego Padres", "SD"], ["San Francisco Giants", "SF"]],
            nl_central: [["Chicago Cubs","CHI"], ["Cincinnati Reds", "CIN"], ["Milwaukee Brewers", "MIL"], ["Pittsburgh Pirates", "PIT"], ["St.Louis Cardinals", "STL"]]
        }

        var styles = {
            headDivision: {
                display: "inline"
            }
        }
    }

    componentDidMount() {
        console.log("HOME");
        console.log(this.state.al_central)
    }

    render() {
        return (
            <div class="home">
                <div className="home-division">
                    <Division className="division" name={"AL East"} teams={this.state.al_east}/>
                    <Division className="division" name={"AL Central"} teams={this.state.al_central}/>
                    <Division className="division" name={"AL  West"} teams={this.state.al_west}/>
                </div>
                <div className="home-division">
                    <Division className="division" name={"NL East"} teams={this.state.nl_east}/>
                    <Division className="division" name={"NL Central"} teams={this.state.nl_central}/>
                    <Division className="division" name={"NL West"} teams={this.state.nl_west}/>
                </div>
            </div>
        )
    }

}