export default function Sidebar() {
    return (
        <div className="flex flex-col h-full w-full bg-transparent">
        <div className="flex items-center justify-center h-20 border-b">
            <h1 className="text-2xl font-bold">Logo</h1>
        </div>
        <div className="flex flex-col p-4">
            <a href="#" className="py-2 text-gray-600 hover:text-gray-800">
            Home
            </a>
            <a href="#" className="py-2 text-gray-600 hover:text-gray-800">
            About
            </a>
            <a href="#" className="py-2 text-gray-600 hover:text-gray-800">
            Services
            </a>
            <a href="#" className="py-2 text-gray-600 hover:text-gray-800">
            Contact
            </a>
        </div>
        </div>
    );
}