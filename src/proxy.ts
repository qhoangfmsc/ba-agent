import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";

/**
 * Middleware — Auth is handled client-side by @vnxdev/auth-react (localStorage).
 * Middleware only handles static file passthrough and basic routing.
 */
export function middleware(request: NextRequest) {
	const { pathname } = request.nextUrl;

	// Allow static files and Next.js internals
	if (
		pathname.startsWith("/_next") ||
		pathname.startsWith("/api") ||
		pathname.includes(".")
	) {
		return NextResponse.next();
	}

	return NextResponse.next();
}

export const config = {
	matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
