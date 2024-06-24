import { NextRequest, NextResponse } from "next/server";
import { UTApi } from "uploadthing/server";

const utapi = new UTApi({
  apiKey: process.env.UPLOADTHING_SECRET,
});

export async function GET(req: NextRequest) {
  try {
    const imgData = await utapi.listFiles();

    let filenames: string[] = [];
    let imgUrls: string[] = [];

    const url = req.nextUrl;
    if (url.searchParams.has("filenames")) {
      filenames = (url.searchParams.get("filenames") as string).split(",");

      filenames.forEach((name) => {
        const file = imgData.files.find(
          (file) => file.name.split(".")[0] === name
        );
        if (file) {
          imgUrls.push(file.key);
        }
      });

      if (imgUrls.length === 0) {
        return NextResponse.json({ message: "No files found." });
      }
      return NextResponse.json(imgUrls);
    }
    return NextResponse.json({ message: "Missing query parameters." });
  } catch (error: any) {
    return NextResponse.json({
      message: "Unable to fetch files.",
      error: error,
    });
  }
}
