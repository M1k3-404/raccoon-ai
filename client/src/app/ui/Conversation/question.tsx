export default function Question(
    props: Readonly<{
        question: string;
    }>
) {
    return (
        <div className="w-[80%] bg-[#80b5d3] p-3 mx-3 mb-1 mt-2 rounded-2xl place-self-end">
            <p className="text-white text-xl">{props.question}</p>
        </div>
    );
}