"use client"

import { Inter } from "next/font/google";
import "./ui/globals.css";
import { Button, NextUIProvider } from "@nextui-org/react";
import { FaCirclePlus } from "react-icons/fa6";
import Image from "next/image";
import Link from "next/link";
import Space from "./ui/images/space.jpg";

const inter = Inter({ subsets: ["latin"] });
import { marvel } from "./ui/fonts";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <NextUIProvider>
        <body className={`${inter.className} bg-cstm-black flex h-screen flex-col md:flex-row md:overflow-hidden`}>
          {/* Sidebar */}
          <div className="w-1/4 h-[96%] my-auto flex flex-col justify-between">
            {/* Header */}
            <div className="flex items-center justify-center rounded-2xl bg-img-cstm-space h-[11%] mx-5">
              <p className={`${marvel.className} text-center z-50 text-7xl tracking-[0.5rem]`}>Raccoon AI</p>
            </div>

            {/* Conversations */}
            <div className="flex flex-col h-[60%] mx-5 rounded-2xl bg-cstm-dark-gray overflow-y-auto">
              <Button as={Link} href="/" className="mt-4 mx-auto p-2 rounded-xl bg-cstm-light-gray w-[90%] h-[9%]">
                <p className="text-white">Conversation</p>
              </Button>
              <Button disabled className="mt-3 flex mx-auto p-2 rounded-xl border border-slate-200 bg-transparent w-[90%] h-[9%]">
                <FaCirclePlus color="white" className="mx-1" />
                <p className="text-white">New Chat</p>
              </Button>
            </div>

            {/* Avatar */}
            <div className="relative mx-5 h-[24%] rounded-2xl bg-white overflow-hidden">
              <Image 
                src={Space}
                alt="Raccoon"
                className="z-0"
                width={2454}
                height={1636}
              />
              <p className={`${marvel.className} absolute top-[45%] left-[50%] z-10 text-white tracking-widest text-5xl mx-auto mb-0`}>
                ROCKET 1.0<br />
                <span className={`${inter.className} text-medium tracking-normal font-normal`}>powered by Gemini 1.0</span>
              </p>
            </div>
          </div>

          {/* Main Content */}
          <div className="flex-grow my-auto items-center w-3/4 h-[96%]">
            <div className="mx-5 h-full rounded-2xl bg-cstm-dark-gray">
              {children}
            </div>
          </div>
        </body>
      </NextUIProvider>
    </html>
  );
}
