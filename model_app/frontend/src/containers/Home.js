import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import {withStyles} from '@material-ui/core';

//import './Home.css';

const styles = {
    imageBox: {
        ///* Here's the trick */
        background: "linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5))", 
        backgroundImage: "url('https://9to5mac.com/wp-content/uploads/sites/6/2020/01/Coronavirus.jpg?quality=82&strip=all')",
        backgroundSize: "cover",
        //backgroundImage: "url('https://images.pexels.com/photos/60597/dahlia-red-blossom-bloom-60597.jpeg?cs=srgb&dl=pexels-pixabay-60597.jpg&fm=jpg')",
    
        ///* Here's the same styles we applied to our content-div earlier */
        color: "white",
        height: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",

        "&:hover": {
            boxShadow: "inset 0 0 0 100vw rgba(0,0,0,0.5)",
        },
    },
    
    Button: {
        "&:hover": {
            color: "black",
            backgroundColor: "#66FCFF",
        },
    },   
};

class Home extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        const {classes} = this.props;
        return (
            <React.Fragment>
                <CssBaseline />
                <div className={classes.imageBox}>
                    <div className={classes.headerText}>
                        <h1>Interactive Disease Simulation</h1>
                        <Button className={classes.Button} variant="contained" color="primary" href="/simulator">
                            Explore Simulation
                        </Button>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default withStyles(styles)(Home);