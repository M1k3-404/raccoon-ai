import Image from 'next/image';
import loader from './ui/images/raccoon (1).png';

export default function Loading() {
    return (
        <div className="w-full h-full animate-pulse">
            <Image
                src={loader}
                alt="loading"
                width={150}
                height={150}
                className="mx-auto pt-[25%]"
            />
        </div>
    )
}