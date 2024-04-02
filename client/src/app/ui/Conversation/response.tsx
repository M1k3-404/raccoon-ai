import { Button } from "@nextui-org/react";
import axios from "axios";
import { useState } from "react";
import { BiDislike, BiLike } from "react-icons/bi";

export default function Response(
    props: Readonly<{
        id: number;
        prompt: string;
        response: string;
    }>
) {
    const [isDiabled, setIsDisabled] = useState(false);
    const [clickedButton, setClickedButton] = useState("");

    const handleTrainModel = async (attribute: string) => {
        try {
            setIsDisabled(true);
            setClickedButton(attribute);

            const response = await axios.post("http://localhost:5000/train_model", {
                prompt: props.prompt,
                attribute: attribute === "safe" ? "safe" : "malicious"
            })

            console.log("Response: ", response);
        } catch (error) {
            console.log("Error: ", error);
        }
    }

    return (
        <div className="w-[80%] bg-transparent flex flex-col mb-3">
            <div className={`w-full bg-[#575757] p-3 mx-3 mb-1 rounded-2xl ${props.response.includes("error occurred") ? "bg-red-400" : ""}`}>
                <p className="text-white text-xl">{props.response}</p>
            </div>

            <div className="flex felx-row">
                <Button className={`bg-[#575757] p-3 ml-3 mr-1 rounded-2xl aspect-square ${clickedButton === "safe" ? "bg-[#80b5d3]" : ""}`} onClick={() => handleTrainModel("safe")} disabled={isDiabled} >
                    <BiLike size={18} color="white" />
                </Button>
                <Button className={`bg-[#575757] p-3 ml-3 mr-1 rounded-2xl aspect-square ${clickedButton === "malicious" ? "bg-[#80b5d3]" : ""}`} onClick={() => handleTrainModel("malicious")} disabled={isDiabled} >
                    <BiDislike size={18} color="white" />
                </Button>
            </div>
        </div>
    )
}