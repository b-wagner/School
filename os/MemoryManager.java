/**
 * Memory Manager
 * By Ben Wagner
 * With help from Jerry Quintero
 * 
 * Last Modified December 12, 2015
 */
import java.util.TreeMap;

public class MemoryManager
{
	TreeMap<Integer, Area> free;
	TreeMap<Integer, Area> used;

	public MemoryManager(int size)
	{
		free = new TreeMap<Integer, Area>();
		used = new TreeMap<Integer, Area>();
		free.put(0, new Area(0, size));
	}

	public Area aquire(int amount)
	{
		int start, key; //Stores start and key values
		Area allocated;
		
		synchronized(used) //Synchronizes the used TreeMap
		{
			if(used.isEmpty())
			{
				start = 0;
				key = 0;
			}
			else
			{
				start = used.get(used.lastKey()).getEnd();
				key = used.lastKey() + 1;
			}
			
			allocated = new Area(start, start + amount);
			used.put(key, allocated);
		}
		
		synchronized(free) //Synchronizes the free TreeMap
		{
			int maxMem = free.lastEntry().getValue().getEnd(); //Determines the maximum amount of memory allowed
			start = 0;
			key = free.lastKey() +  1;
			free.put(key,  new Area(start, (maxMem - amount)));
		}
		
		return allocated;
	}

	public void release(int handle)
	{
		Area remove = null;
		synchronized(used) //Synchronizes the used TreeMap
		{
			if(used.isEmpty())
			{
				return;
			}

			int size = used.size();
			for(int i = 0; i <= size; i++)
			{
				if(used.get(i) == null)
				{
					continue;
				}
				else if(used.get(i).getStart() == handle)
				{
					remove = used.get(i);
					used.remove(i);
					break;
				}
			}
		}
		synchronized(free) //Synchronizes the free TreeMap
		{
			//Revert back to first entry if this Area variable is null
			if(remove != null)
			{
				int start = free.firstEntry().getValue().getStart();
				free.firstEntry().getValue().setStart(start - remove.getSize());
			}
		}
	}

	public void print()
	{
		synchronized (free)
		{
			System.out.println("\nFree");
			free.forEach((k, v) -> System.out.println(k + "->" + v.getEnd() + "(" + v.getSize() + ")"));
			System.out.println("Used");
			used.forEach((k, v) -> System.out.println(k + "->" + v.getEnd() + "(" + v.getSize() + ")"));
		}
	}

	public Area getFirstFree()
	{
		return free.firstEntry().getValue();
	}
}