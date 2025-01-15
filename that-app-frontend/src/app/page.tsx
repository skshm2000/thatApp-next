"use client";
import { useMutation } from "@tanstack/react-query";
import { Button, Input } from "antd";
import { useState } from "react";

interface UserDetails {
  name: string;
  number: number | null;
}

export default function Home() {
  const [userDetails, setUserDetails] = useState<UserDetails>({
    name: "",
    number: null,
  });
  const createUserRequest = useMutation({
    mutationFn: async () => {
      const response = await fetch("http://127.0.0.1:8000/thatApp/create", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userDetails),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      return response.json();
    },
    onSuccess: (data) => {
      console.log(data, 1111);
    },
  });
  return (
    <div className="flex flex-col gap-4 w-1/2 border border-solid border-gray-300 rounded-lg p-6">
      <div className="flex flex-col gap-2">
        <span>Enter name</span>
        <Input
          placeholder="Enter name"
          onChange={(e) =>
            setUserDetails({ ...userDetails, name: e.target.value })
          }
        />
      </div>
      <div className="flex flex-col gap-2">
        <span>Enter phone number</span>
        <Input
          placeholder="Enter phone number"
          onKeyDown={(e) => {
            if (e.key === "Backspace" || e.key === "Enter") return;
            if (!"0123456789".includes(e.key)) e.preventDefault();
          }}
          onChange={(e) =>
            setUserDetails({ ...userDetails, number: Number(e.target.value) })
          }
          minLength={10}
        />
      </div>
      <Button onClick={() => createUserRequest.mutate()}>Create account</Button>
    </div>
  );
}
