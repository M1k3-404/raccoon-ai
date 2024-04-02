import { RxDotsHorizontal } from "react-icons/rx";

export default function ResponseLoading() {
    return (
        <div className="w-[10%] bg-[#575757] p-3 mx-3 mb-3 rounded-2xl animate-pulse">
            <RxDotsHorizontal size={28} />
        </div>
    )
}