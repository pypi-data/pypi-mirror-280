import Homepage from "@/pages/Homepage";
import { Suspense } from "react";

export default function Home() {
  return (
    <Suspense fallback={<></>}>
      <Homepage />
    </Suspense>
  );
}
