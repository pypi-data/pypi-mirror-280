import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function zip(...arrays: any[]) {
  const minLength = Math.min(...arrays.map((arr) => arr.length));
  return Array.from({ length: minLength }, (_, i) =>
    arrays.map((array) => array[i])
  );
}

export function title(item: string) {
  return item[0].toUpperCase() + item.substring(1, item.length);
}
