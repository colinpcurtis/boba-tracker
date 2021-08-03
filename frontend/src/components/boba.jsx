import React, {useState} from 'react'

const Boba = () => {
    const [items, setItems] = useState("")

    const getBoba = async () => {
        const r = await fetch("http://localhost:8000/boba", {
            method: "GET",
        })
        const json = await r.json()
        console.log(json)
        setItems(json)
    }

    if (items === "") {
        getBoba()
    }

    const displayCount = () => {
        return (
            <div>
                <center><h1>The boba count is:</h1></center>
                {Object.keys(items).map((name) => (
                    <center><p key={name}>{name} got boba {items[name]} {items[name] === 1  ? "time" : "times"}</p></center>
                ))}
            </div>
        )
    }

    getBoba()

    return (
        <div>
           {displayCount()}
        </div>
    )
}

export default Boba;
