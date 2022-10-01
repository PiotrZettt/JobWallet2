import React from 'react';
import axios from 'axios';

const baseURL = '127.0.0.1:8000/api/';


export default function Wallets() {

    const [walletsData, setWalletsData] = React.useState("")


    axios.get(baseURL + 'wallets' ).then(function(response) {
        setWalletsData = response.data
    }
    )

    return <div>
        <h3>{data.customer}</h3>
        <h3>{data.order_number}</h3>
    </div>
};
