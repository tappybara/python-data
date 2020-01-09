import React from 'react'
import './page.scss'

export class Starts extends React.Component {
    constructor(props){
        super(props)
    }

    componentDidMount(){
        const pid = this.props.match.params.pid

        const spawn = require("child_process").spawn;
        const process = spawn('python', ["../scripts/previous_starts.py", pid])

        process.stdout.on('data', (dates) => {
            console.log(dates);
        })
    }

    render() {
        return (
            null
        )
    }
}