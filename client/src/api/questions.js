import axios from "axios";

export default async function handler(req, res) {
    try {
        const { question, response } = req.body;

        const backendResponse = await axios.post("http://localhost:3001/questions", {
            question,
            response,
        });

        res.status(200).json(backendResponse.data);
    } catch (error) {
        console.error("Error forwading to the backend: ", error);
        res.status(500).json({ message: "Internal server error" });
    }
}