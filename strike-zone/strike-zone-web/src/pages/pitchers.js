import React from 'react'
import {withFirebase} from '../components/Firebase';


import {PitcherCols} from '../components/pitcher_cols.js'
import './page.scss'

class PitchersBase extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            loading: false,
            starters: null,
            bullpen: [],
            closers: [],
        }

        this.getPitchers = this.getPitchers.bind(this);
    }

    componentDidMount() {
        console.log("HOME");
        console.log(this.state.al_central);

        this.getPitchers();
    }

    getPitchers() {
        const team = this.props.match.params.tn
        console.log("YO")
        console.log(team)

        this.props.firebase.pitchers("LAD").on('value', snapshot => {
            const object = snapshot.val();

            if (object) {
                const pitcherList = Object.keys(object).map(key => ({
                    ...object[key]
                }));
                console.log(pitcherList)

                const st = pitcherList.filter(player => player.type === "starter");
                const bp = pitcherList.filter(player => player.type === "bullpen");
                const cl = pitcherList.filter(player => player.type === "closer");
                console.log(st)
                this.setState(
                    {
                    starters: st,
                    bullpen: bp,
                    closers: cl,
                    },
                    () => console.log(this.state)
                );
                    
            }
        })
    }

    componentWillUnmount() {
        this.props.firebase.pitchers("LAD").off();
    }

    render() {
        console.log("RENDER")
        return (
            this.state.starters ?
            <div className="pitchers">
                <div className="pitchers-col">
                    <PitcherCols className="division" name={"Starters"} players={this.state.starters}/>
                </div>
                <div className="pitchers-col">
                    <PitcherCols className="division" name={"Bullpen"} players={this.state.bullpen}/>
                </div>
                <div className="pitchers-col">
                    <PitcherCols className="division" name={"Closers"} players={this.state.closers}/>
                </div>
            </div>
            : <div>Loading...</div>
        )
    
    }
}

const Pitchers = withFirebase(PitchersBase);
export {Pitchers}
